with open('p9.txt', 'r') as f:
    input_s = f.read()

numbers = list(map(int, input_s.split('\n')))

preamble_len = 25
preamble = numbers[:preamble_len]

key = None
for n in numbers[preamble_len:]:
    if not any([(n - x) in preamble and x != n - x for x in preamble]):
        print(n)
        key = n
        break
    preamble = preamble[1:] + [n]


# Use a window to find the contiguous range of numbers
# If the sum is currently lower, then extend window forward
# If the sum is higher, then retract window from the back
window_start = 0
window_end = 0
current_sum = numbers[0]
while True:
    if window_end >= len(numbers):
        print("Reached the end and failed.")
        break
    if current_sum == key:
        print("Success")
        setrange = numbers[window_start:window_end]
        print(min(setrange) + max(setrange))
        break
    elif current_sum < key:
        window_end += 1
        current_sum += numbers[window_end]
        continue
    else:
        current_sum -= numbers[window_start]
        window_start += 1