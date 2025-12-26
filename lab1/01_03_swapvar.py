def convert_string_to_tuples(text_in):
  values = text_in.strip('()').split(', ')
  return tuple(map(float, values))

data = convert_string_to_tuples(input())
a, b = data
a, b = b, a

print((a, b))