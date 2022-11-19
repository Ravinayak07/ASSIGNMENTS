# Question 1

```java
import java.util.*;
public class Question1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Phone number: ");
        String num = sc.nextLine();
        num = num.toUpperCase();
        System.out.print(finalNum(num));
    }
    public static String finalNum(String num) {
        long number = 0;
        int len = num.length();
        String res = "";
        for (int i = 0; i < len; i++) {
            char letter = num.charAt(i);
            if (Character.isDigit(letter)) {
                res = res + letter;
            }
            if (Character.isLetter(letter)) {
                if (letter == 'A' || letter == 'B' || letter == 'C')
                    number = 2;
                else if (letter == 'D' || letter == 'E' || letter == 'F')
                    number = 3;
                else if (letter == 'G' || letter == 'H' || letter == 'I')
                    number = 4;
                else if (letter == 'J' || letter == 'K' || letter == 'L')
                    number = 5;
                else if (letter == 'M' || letter == 'N' || letter == 'O')
                    number = 6;
                else if (letter == 'P' || letter == 'Q' || letter == 'R' || letter == 'S')
                    number = 7;
                else if (letter == 'T' || letter == 'U' || letter == 'V')
                    number = 8;
                else
                    number = 9;
                res = res + number;
            }
        }
        return res;
    }
}
```

# Question 3:

```py
# function Defination
def triple_and(first, second, third):
    result = first and second and third
    return result

x = triple_and(True, True, True)
print(x)  # True as all params are true

y = triple_and(True, True, False)
print(y)  # False as the third param is false

```

# Question 4:

```py
# function defination
def checkList(sampleList):

    element = sampleList[0]
    flag = True

    # Comparing each element of list with first item
    for item in sampleList:
        if element != item:
            flag = False
            break

    if (flag == True):
        print("All elements are Equal")
    else:
        print("All elements are Not equal")


list1 = [1, 2, 3]
checkList(list1)   # Not Equal

list2 = [2, 2, 2]
checkList(list2)   # Equal

```

# Question 5

## 5.1 Reverse_Order

```py
arr = [10, 20, 30, 40, 50]

print("Array is :", arr)

result = arr[::-1]
print("Reversed array:", result)

```

## 5.2 Merge_Two_sorted_arrays

```py
# function defination
def mergeSortedArrays(arr1, arr2, n1, n2, final):
    i = 0
    j = 0
    k = 0

    # traversing arr1 and inserting in final array
    while (i < n1):
        final[k] = arr1[i]
        k = k + 1
        i = i + 1

   # traversing arr2 and inserting in final array
    while (j < n2):
        final[k] = arr2[j]
        k = k + 1
        j = j + 1
    final.sort()  # sorting the final array


arr1 = [10, 30, 50, 70, 90]
n1 = len(arr1)

arr2 = [20, 40, 60, 80]
n2 = len(arr2)

final = [0] * (n1+n2)

mergeSortedArrays(arr1, arr2, n1, n2, final)

print("After merging: ")

for i in range(n1 + n2):
    print(final[i], end=" ")

```

## 5.3 Nth_fibonacci

```py
# function defination:
def fibonacci(n):

    a, b = 0, 1

    if (n == 1):
        return 0

    elif (n == 2):
        return 1

    for i in range(n-2):
        temp = a + b
        a = b
        b = temp
    return temp


print(fibonacci(9))

```
