def ED(first, second):
   ''' Returns the edit distance between the strings first and second.'''
   if first == '': 
      return len(second)
   elif second == '':
      return len(first)
   elif first[0] == second[0]:
      return ED(first[1:], second[1:])
   else:
      substitution = 1 + ED(first[1:], second[1:])
      deletion = 1 + ED(first[1:], second)
      insertion = 1 + ED(first, second[1:])
      return min(substitution, deletion, insertion)


def fastED(s1,s2):
    
    def fastEDHelper(s1,s2,memo):
        
        if memo.has_key((s1,s2)):
            return memo[(s1,s2)]
        
        if s1=='':
            result= len(s2)
            return result
        if s2=='':
            result= len(s1)
            return result

        elif s1[0]==s2[0]:
            result=fastEDHelper(s1[1:],s2[1:],memo)
            
        else:
            subsitution=1+fastEDHelper(s1[1:],s2[1:],memo)
            deletion=1+fastEDHelper(s1[1:],s2,memo)
            insertion=1+fastEDHelper(s1, s2[1:],memo)
            result= min(subsitution, deletion, insertion)
            memo[(s1,s2)]=result
        return result
    return fastEDHelper(s1,s2,{})

            

    

            
    


    
    


