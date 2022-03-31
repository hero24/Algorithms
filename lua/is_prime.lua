-- "The way to get started is to quit talking and begin doing."
--      -Walt Disney

function is_prime(num)
        if num <=3 then
                return num > 1
        elseif num % 2 == 0 or num % 3 ==0 then
                return false
        end
        i = 5
        while i ^ 2 <= num do
                if num % i == 0 or num % (i + 2) == 0 then
                        return false
                end
                i = i + 6
        end
        return true
end
