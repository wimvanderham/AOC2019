import time

def password_ok (password):

    ok = False

    
    if len(password) == 6:
        if  int(password[0]) <= int(password[1]) and int(password[1]) <= int(password[2]) and int(password[2]) <= int(password[3]) and int(password[3]) <= int(password[4]) and int(password[4]) <= int(password[5]):
            if password[0] == password[1] or password[1] == password[2] or password[2] == password[3] or password[3] == password[4] or password[4] == password[5]:
                #print password
                ok = True

    return ok


def password_ok2 (password):
    # Check password ok according to second part
    
    ok = False

    
    if len(password) == 6:
        if  int(password[0]) <= int(password[1]) and int(password[1]) <= int(password[2]) and int(password[2]) <= int(password[3]) and int(password[3]) <= int(password[4]) and int(password[4]) <= int(password[5]):
            for char in range(len(password)):
                if char == 0:
                    group = password[char]
                else:
                    if password[char] == group[0]:
                        group += password[char]
                    else:
                        if len(group) == 2:
                            ok = True
                        group = password[char]
            
            if len(group) == 2:
                ok = True
                
    return ok


start_time = time.time()

start = 246540
end   = 787419

nr_passwords  = 0
nr_passwords2 = 0

for password_nr in range(start, end + 1):
    #print password_nr
    if password_ok(str(password_nr)) == True:
        nr_passwords += 1
        #print nr_passwords, password_nr
        
    if password_ok2(str(password_nr)) == True:
        nr_passwords2 += 1
        
end_time = time.time()

print "Solution 1:", nr_passwords
print "Solution 2:", nr_passwords2
print "Solution found in:", (end_time - start_time)
