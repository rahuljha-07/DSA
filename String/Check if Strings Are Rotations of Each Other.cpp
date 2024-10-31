bool areRotations(string s1,string s2){
	if(s1.size()!=s2.size())  return false;
	
    string concat = s1+s1;
	int ind = concat.find(s2);
	if(ind==-1) return false;
	return true;
}