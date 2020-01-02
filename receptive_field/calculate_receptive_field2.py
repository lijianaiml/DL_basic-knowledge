import math


def cal_receptive_field_top_2_down(k, s):
  rf = 1
  for i in range(len(k)):
    rf = k[i] + s[i] * (rf - 1)
    print(rf)

  print("layers:", len(k))
  print(rf)


def cal_receptive_field_down_2_top(k, s):
  s.reverse()
  k.reverse()

  R = k[0]
  S = s[0]
  print("layers: 1")
  print(R)
  for i in range(1, len(k)):
    R = R + (k[i] - 1) * S
    S = S * s[i]
    print("layers:", str(i + 1))
    print(R)


def get_padding(k, s, size):
  k.reverse()
  s.reverse()
  n_in = 256
  padding = []
  for i in range(len(size)):
    actualP = (size[i] - 1) * s[i] - n_in + k[i]
    p = math.ceil(actualP / 2)
    n_in = size[i]
    padding.append(p)
  return padding


if __name__ == '__main__':

  # scale 1 order by top_2_down
  k = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3,
       1, 3, 1, 3, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 3, 1, 3, 1, 3, 3, 1, 3, 3]
  s = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1]

  # output size order by down_2_top
  size = [256, 128, 128, 128, 64, 64, 64, 64, 64, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 16,
          16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8]

  # scale 3 order by top_2_down
  # k = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 3, 1, 3, 1, 3, 3, 1, 3, 3]
  # s = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1]

  # cal_receptive_field_top_2_down(k, s)

  cal_receptive_field_down_2_top(k, s)

  # p = get_padding(k, s, size)
