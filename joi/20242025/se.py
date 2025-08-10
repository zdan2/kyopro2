# n: アイテム数, c: 予算
n, c = map(int, input().split())
# a: 各アイテムのコスト
a = list(map(int, input().split()))
# p_raw: 各アイテムの親（前提アイテム）、1-indexed, -1はルート
p_raw = list(map(int, input().split()))

# 前提アイテムの指定にルート（-1）が一つもなければ、どのアイテムも取得不可能
if -1 not in p_raw:
    print(0)
    exit()

# 親リストを1-indexedから0-indexedに変換して扱いやすくする
p = [val - 1 if val != -1 else -1 for val in p_raw]

# 到達可能な全経路を探索する
paths = []
# これから処理すべきノードの集合
nodes_to_process = set(range(n))

while nodes_to_process:
    # 未処理のノードのうち、インデックスが最大のものから探索を開始する
    start_node = max(nodes_to_process)
    
    current_path = []
    # 今回の探索で訪れたノードを記録し、サイクルを検出する
    visited_in_this_trace = set()
    current_node = start_node
    
    is_cyclic = False
    # ルート(-1)に到達するまで親をたどる
    while current_node != -1:
        # 今回の探索中に同じノードを再び訪れた場合、サイクルになっている
        if current_node in visited_in_this_trace:
            is_cyclic = True
            break
        
        visited_in_this_trace.add(current_node)
        current_path.append(current_node)
        
        # 経路上のノードは処理済みとし、探索開始点から除外する
        nodes_to_process.discard(current_node)
        
        current_node = p[current_node]

    # サイクルに陥らず、正しくルートに到達した経路のみを保存する
    if not is_cyclic:
        paths.append(current_path)

# 全ての有効な経路について、予算内で到達できる最も遠いノードを探す
max_reachable_node = -1

for path in paths:
    capacity = c
    last_affordable_node_on_this_path = -1
    
    # アイテムを取得するには、その前提アイテムをすべて取得する必要がある
    # そのため、経路をルート側から順にたどる (pathをreverseする)
    for node in reversed(path):
        # 予算がアイテムのコスト以上なら取得できる
        if capacity >= a[node]:
            capacity -= a[node]
            last_affordable_node_on_this_path = node
        else:
            # 予算が足りなければ、この先のアイテムは取得できない
            break
            
    # 全ての経路の中で、到達できた最も大きいインデックスのノードを更新する
    max_reachable_node = max(max_reachable_node, last_affordable_node_on_this_path)

# 問題の要求は1-indexedの答え。何も到達できなければmax_reachable_nodeは-1なので、-1 + 1 = 0 となる
print(max_reachable_node + 1)