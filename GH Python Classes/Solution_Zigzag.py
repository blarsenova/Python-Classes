class Solution(object):
    def convert(self, s, numRows):
        # If only one row or string is too short, no zigzag is possible
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize rows as empty strings
        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char

            # Switch direction if we hit the top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move to the next row
            current_row += 1 if going_down else -1

        # Join all rows into a single string
        return "".join(rows)