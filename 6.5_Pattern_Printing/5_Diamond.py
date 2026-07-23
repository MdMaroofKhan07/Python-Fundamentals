'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

rows = 5

# Upper half
for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1

    print("  " * spaces, end="")
    print("* " * stars)

# Lower half
for i in range(rows - 1, 0, -1):
    spaces = rows - i
    stars = 2 * i - 1

    print("  " * spaces, end="")
    print("* " * stars)