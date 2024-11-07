

def mod_exp(base,exp,mod):
    return pow(base,exp,mod)

def main():
    q,alpha = int(input("Enter q : ")) ,int(input("Enter alpha: "))
    X_A,X_B = int(input("Enter Alice's X_A: ")), int(input("Enter Bob's X_B: "))
    
    Y_A,Y_B = mod_exp(alpha,X_A,q),mod_exp(alpha,X_B,q)
    shared_A,shared_B = mod_exp(Y_B,X_A,q) , mod_exp(Y_A,X_B,q)
    
    print(f"alices public key : {Y_A},Bobs public key : {Y_B}")
    print(f"Shared key: {shared_A}" if shared_A == shared_B else "Error in computing shared key")
    
    
if __name__ == "__main__":
    main()

    