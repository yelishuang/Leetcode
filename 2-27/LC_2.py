# 超出时间限制，动态规划问题，结合官方案例解析
# 使用贪心思路发现其实是想多了，也不一定需要动态规划解决，主要是求上升区间和问题因为前一天买后一天卖而且知道全部信息，不需要考虑持有成本问题，只需要在上升区间前买， 上升区间后卖即可

def maxProfit(self,prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    return sum([prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i+1]-prices[i] > 0 ])

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) <=1:
        return 0
    value=[]
    for i in range(len(prices) - 1 ):
        value.append([])
        for j in range(i+1, len(prices)):
            value[i].append((prices[j]-prices[i]) if (prices[j]-prices[i]) >= 0 else -1)
    value_max = [ ]
    j=0
    for i in range(len(value)):
        temp = []
        for j in range(i,-1,-1):
            if value[i-j][j] <= 0:
                continue
            else:
                row = 0 
                max_row = value[i-j][j]
                while row < i-j:
                    max_row = value[i-j][j]+value_max[row] if  value[i-j][j]+value_max[row] > max_row else max_row
                    row = row+1
                temp.append(max_row)                
        if len(temp)== 0:
            value_max.append(0)
        else:
            value_max.append(max(temp))
    return max(value_max)

if __name__=="__main__":
    prices = [7,6,4,3,1]
    print(maxProfit(prices))
                                   

    
