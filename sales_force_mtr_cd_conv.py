from collections import defaultdict

def find_conv_val(inp_std, src_unit,dst_unit):
    adj_list=defaultdict(list)
    for src,dst,unt in inp_std:
        adj_list[src].append((dst,unt))
        adj_list[dst].append((src, round(1/unt,4)))
    # print(adj_list)

    def dfs(adj_list,src,dst,amt,visited):
        if src is None:
            return
        if src == dst:
            return amt
        if src not in visited:
            visited.add(src)
            for new_dst,new_amt in adj_list[src]:
                fin_amt=dfs(adj_list,new_dst,dst,amt+new_amt,visited)
                if fin_amt:
                    return fin_amt
        else:
            return
        return -1

    dfs(adj_list,src_unit,dst_unit,0,set())


inp_conv_std=[('km','mtr',1000),('mtr','cm',100),('cm','mm',10),('ft','in',12),('in','cm',2.54),('mtr','ft',3.28084)]
print(find_conv_val(inp_conv_std,'km','cm'))
# print(find_conv_val(inp_conv_std,'km','mtr'))
# print(find_conv_val(inp_conv_std,'mtr','in'))