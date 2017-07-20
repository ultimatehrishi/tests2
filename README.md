# Write a program to compress the string? 

   Input Format

   A single line of input consisting of the string .

   Output Format

   A single line of output consisting of the modified string.

   Examples-Input

   abbbccddaaab

   Sample Output

   a1b3c2d2a3b1

   Explanation:

   a is repeated 1 time so 'a1' followed by b which is repeated 3 times so 'a1b3' etc


    def compress(input_str):
             

       return compressed_output_str 

# Write a program to generate fibonacci series using recurssion ( No Use of Loops)
    Fab Series = 1, 1, 2, 3, 5, 8, 13 ....

    def fab(length):
        return series

    Example-input
    fab(4)
    Example-output
    [1,1,2,3]

    Example-input
    fab(6)
    Example-output
    [1,1,2,3,5,8]

# Write a program "tail" which works for these scenarios

    tail -5 file1.txt  - should give the last 5 lines of the file file1.txt

    tail -3 file3.txt  - should give last 3 lines of file file3.txt

    tail  3 file.txt  - should give first 3 lines of file.txt

    tail -10 file1.txt -20 file2.txt - should give last 10 lines of file1.txt and last 20 lines of file file2.txt

    tail file.text - Full content of the file

# Normalise the following example database table, highlight all the keys, and describe all the relationships:

  Customer         Addresss                  City    Post_Code  Invoice         Date  Item     Description           Qty  Price   Total    Order_Total
  ---------------  ------------------------  ------  ---------  -------  -----------  -------  --------------------  ---  ------  -------  -----------
  Fighters of Foo  44, Wardour Street, Soho  London  W1A 4AA        124  16-Feb-2010  Widget   8x2 Spangly Widget      2   40.00    80.00       280.00
  Fighters of Foo  44, Wardour Street, Soho  London  W1A 4AA        124  16-Feb-2010  Gadgets  Plain Gadget, 4 pack    1  100.00   100.00       280.00
  Fighters of Foo  44, Wardour Street, Soho  London  W1A 4AA        124  16-Feb-2010  Radget   Red Gadget, Glossy     10   10.00   100.00       280.00
  Foxes of Fleet   The Sanctuary, High St    Exeter  EX2 3BZ        199  21-Feb-2010  Radget   Red Gadget, Glossy     40   10.00   400.00      3000.00
  Foxes of Fleet   The Sanctuary, High St    Exeter  EX2 3BZ        199  21-Feb-2010  Gadget   Plain Gadget, 4 pack   10  100.00  1000.00      3000.00
  Foxes of Fleet   The Sanctuary, High St    Exeter  EX2 3BZ        199  21-Feb-2010  Widget   8x2 Spangly Widget     40   40.00  1600.00      3000.00

  This DB question is subjective question, no coding required