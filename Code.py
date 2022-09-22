Candidate_1="Python"
Candidate_2="Rust"
print("First candidate is:",Candidate_1)
print("Second candidate is:",Candidate_2)

cand1_votes=0
cand2_votes=0

voters_id=[1,2,3,4,5,6,7,8,9,10]

num_of_voter=len(voters_id)
print("Number of voters:",num_of_voter)
voted=[]

while True:
    if voters_id==[]:
        print("Voting Session over")
        if cand1_votes>cand2_votes:
            percent=(cand1_votes/num_of_voter)*100
            print(Candidate_1,"has won with",percent,"% votes")
            break
        elif cand2_votes>cand1_votes:
            percent=(cand2_votes/num_of_voter)*100
            print(Candidate_2,"has won with",percent,"% votes")
            break
        elif cand1_votes==cand2_votes:
            print("Tied !!!")
            break
    
    else:


        voter=int(input("Enter your voter id no:"))
        if voter in voted:
            print("You already voted")
       
        else:
            if voter in voters_id:
                print(f"1.{Candidate_1}\n2.{Candidate_2}") 
                choice= int(input("Enter your choice:"))       
                if choice==1:
                    cand1_votes+=1
                    print(f"You voted {Candidate_1}")
                elif choice==2:
                    cand2_votes+=1
                    print(f"You voted {Candidate_2} ")
                voters_id.remove(voter)
                voted.append(voter)
            else:
                print("You are not allowed to vote")





                
            
    

 


