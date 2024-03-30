def phan_tu_nhieu_hon_k_lan(L, k):
    # Tạo dictionary đếm số lần xuất hiện của từng phần tử trong list L
    counts = {num: L.count(num) for num in set(L)}

    # Tạo list kết quả chứa các phần tử xuất hiện nhiều hơn k lần
    L_kq = [num for num, count in counts.items() if count > k]

    # Sắp xếp list kết quả theo thứ tự tăng dần
    L_kq.sort()

    return L_kq

# Ví dụ sử dụng:
L = [1, 2, 3, 2, 3, 4, 5, 4, 6, 7, 6, 8, 9, 8]
k = 2
result = phan_tu_nhieu_hon_k_lan(L, k)
print("Các phần tử xuất hiện nhiều hơn", k, "lần trong list L: ", result)
