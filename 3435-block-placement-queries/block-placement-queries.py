from sortedcontainers import SortedList
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        sl = SortedList([0])
        N = 5*(10**4)
        tree = [0]*(4*N)
        def query(tree,v,tl,tr,l,r):
            if r < tl or tr < l:
                return 0
            elif l<=tl and tr<=r:
                return tree[v]
            else:
                m = (tl+tr)//2
                return max(query(tree,2*v,tl,m,l,r), query(tree,2*v+1,m+1,tr,l,r))

        def update(tree,v,tl,tr,idx,val):
            if tl==idx==tr:
                tree[v]=val
                return val
            mid = (tl+tr)//2    
            if tl<=idx<=mid:
                tree[v]=max(update(tree,2*v,tl,mid,idx,val),tree[2*v+1])
            else:
                tree[v]=max(tree[2*v],update(tree,2*v+1,mid+1,tr,idx,val))
            return tree[v]        
        res = []
        for q in queries:
            if q[0] == 1:
                i = sl.bisect_left(q[1])
                if i == len(sl):
                    idx = sl[-1]
                    update(tree, 1, 0, N-1, idx, q[1]-idx)
                else:
                    idx = sl[i-1]
                    update(tree, 1, 0, N-1, idx, q[1]-idx)
                    update(tree, 1, 0, N-1, q[1], sl[i]-q[1])
                sl.add(q[1])
            else:
                _, x, sz = q
                i = sl.bisect_left(x)
                #print("sl, i", sl, i)
                widest = x-sl[i-1]
                if i == 1:
                    left = 0
                else:
                    left = query(tree, 1, 0, N-1, 0, sl[i-1]-1)
                res.append(max(widest, left)>=sz)
        return res
