def IntToRoman(num):
        def thousandths_place(s):
            if s[0] in ['1','2','3']:
                return 'M'*int(s[0])
        def hundredths_place(s, index):
            if s[index] in ['1','2','3']:
                return 'C'*int(s[index])
            elif s[index] == '4':
                return 'CD'
            elif s[index] == '5':
                return 'D'
            elif s[index] in ['6','7','8']:
                return 'D'+'C'*eval(s[index]+'-5')
            elif s[index] == '9':
                return 'CM'
            else:
                return ''
        def tens_place(s, index):
            if s[index] in ['1','2','3']:
                return 'X'*int(s[index])
            elif s[index] == '4':
                return 'XL'
            elif s[index] == '5':
                return 'L'
            elif s[index] in ['6','7','8']:
                return 'L'+'X'*eval(s[index]+'-5')
            elif s[index] == '9':
                return 'XC'
            else:
                return ''
        def ones_place(s, index):
            if s[index] in ['1','2','3']:
                return 'I'*int(s[index])
            elif s[index] == '4':
                return 'IV'
            elif s[index] == '5':
                return 'V'
            elif s[index] in ['6','7','8']:
                return 'V'+'I'*eval(s[index]+'-5')
            elif s[index] == '9':
                return 'IX'
            else:
                return ''
        roman = str(num)
        digits = len(roman)
        if digits == 1:
            return ones_place(roman,0)
        elif digits == 2:
            return tens_place(roman,0) + ones_place(roman,1)
        elif digits == 3:
            return hundredths_place(roman,0) + tens_place(roman,1) + ones_place(roman,2)
        else:
            return thousandths_place(roman) + hundredths_place(roman,1) + tens_place(roman,2) + ones_place(roman,3)
"""print(IntToRoman(3))
print(IntToRoman(4))
print(IntToRoman(9))
print(IntToRoman(58))
print(IntToRoman(1994))"""
import LeetCode as a
print(a.ha())
