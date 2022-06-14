/* 

Solution to Problem "Valid Parentheses" on LeetCode
A. K. Nguyen
Boston University 2022

Runtime: 557 ms
Memory Usage: 158.4 MB
 
*/

import java.util.*;
class ValidParentheses {
    public boolean isValid(String s) {
        
        Stack<Character> STACK = new Stack<Character>();
            
        for (int i = 0; i < s.length(); i++)
        {
            if (s.charAt(i) == '{' || s.charAt(i) == '(' || s.charAt(i) == '[')
            {
                STACK.push(s.charAt(i));
                System.out.println(Arrays.toString(STACK.toArray()));
            }
            else
            {
                if (STACK.size() == 0)
                {
                    return false;
                }
                char current_char = STACK.pop();
                if (current_char == '{')
                {
                    if (s.charAt(i) != '}')
                    {
                        return false;
                    }
                }
                if (current_char == '[')
                {
                    if (s.charAt(i) != ']')
                    {
                        return false;
                    }
                }
                if (current_char == '(')
                {
                    if (s.charAt(i) != ')')
                    {
                        return false;
                    }
                }
            
            }
            
        }
        if (STACK.size() != 0)
        {
            return false;
        }
        else
        {
            return true;
        }

        
    }
}
