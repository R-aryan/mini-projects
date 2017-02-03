#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

class vehicle
{

public:
    string name;
    int rno;

};

template<class t1, class t2>
void print(t1 x , t2 y)
{
if(y=='A')
cout<<"Slot A is available for car parking and Slot B is full and remaining space is \t"<<10- x.size()<<"\n\n";
else if(y=='B')
cout<<"Slot B is available for car parking and Slot A is full and remaining space is  \t"<<10- x.size()<<"\n\n";
else if(y=='C')
cout<<"Slot C is available for Scooter parking and Slot D is full and remaining space is \t"<<10- x.size()<<"\n\n";
else if(y=='D')
cout<<"Slot D is available for Scooter parking and Slot C is full and remaining space is \t"<<10- x.size()<<"\n\n";
else if(y=='a')
cout<<"Slot A is available for car parking  and remaining space is \t"<<10- x.size()<<"\n\n";
else if(y=='b')
cout<<"Slot B is available for car parking  and remaining space is \t"<<10- x.size()<<"\n\n";
else if(y=='c')
cout<<"Slot C is available for Scooter parking  and remaining space in the slot is \t"<<10- x.size()<<"\n\n";
else if(y=='d')
cout<<"Slot D is available for Scooter parking and remaining space in the slot is \t"<<10-x.size()<<"\n\n";





}


int main()
{
    vehicle v,vt;
    queue<vehicle>a;
    queue<vehicle>b;
    vector<vehicle>c,d,v1,v2;
    string na;
    int ch,r,q;
    cout<<"\t\t\t Vehicle Parking Facility \n";
    cout<<"\t\t\t **************************** \n\n";


    do
    {
        
        cout<<"\t\t enter your choice \n\n";
        cout<<"\t\t Press 1 for car parking \n\n"<<"\t\t Press 2 for scooter parking \n\n";
        cout<<"\t\t Press 3 to remove your vehicle from parking \n\n"<<"\t\t Press 4 to know the current status of parking slots";
        cin>>ch;
        switch(ch)
        {
            case 1:
                cout<<"enter your car name and registration number\n";
                cin>>v.name>>v.rno;
            if(a.size()<10)
            {
                 cout<<"your parking slot is A \n"<<"And your slot number is \t"<<a.size()+1;cout<<"\n";
                 a.push(v);
                 v1.push_back(v);

                 //vehicle vc=a.front();
                 //cout<<vc.name<<"\n";
                 }
                 else if(b.size()<10)
                 {
                 cout<<"your parking slot is B \n"<<"And your slot number is \t"<<b.size()+1<<"\n";
                 b.push(v);
                 v1.push_back(v);
                 }

                 else
                    cout<<"sorry no parking space available please try after some time \n";
                 break;
            case 2:
                 cout<<"enter name and registration number of your vehicle \n";
                cin>>v.name>>v.rno;
            if(c.size()<10)
            {
                 cout<<"your parking slot is C \n"<<"And your slot number is \t"<<c.size()+1<<"\n";
                 c.push_back(v);
                 v2.push_back(v);

                 //vehicle vc=a.front();
                 //cout<<vc.name<<"\n";
                 }
                 else if(d.size()<10)
                 {
                 cout<<"Your parking slot is D \n"<<"And your slot number is \t"<<d.size()+1<<"\n";
                 d.push_back(v);
                 v2.push_back(v);
                 }

                 else
                    cout<<"sorry no parking space available please try after some time \n";
                 break;
            case 3:
                cout<<"Select Your vehicle type to remove it from parking slot \n";
                cout<<"Press S for scooter \n"<<"Press C for car\n";
                char ch1;cin>>ch1;
                switch(ch1)
                {
                    case 'C':
                    int co;
                    if(a.size()<=10)
                    {
                        vt=a.front();
                        cout<<"Your registration number is "<<vt.rno<<"\n";
                        cout<<"press 1 to proceed \n";cin>>co;
                        if(co==1)
                            a.pop();


                    }
                    else if(b.size()==10)
                    {
                        vt=b.front();
                        cout<<"Your registration number is "<<vt.rno<<"\n";
                        cout<<"press 1 to proceed \n";cin>>co;
                        if(co==1){
                            b.pop();
                            cout<<"Vehicle successfully removed from queue\n";}
                    }
                    break;
                    case 'S':
                        int choice;char sl;
                        cout<<"enter a valid slot name and slot number \n";
                        cin>>sl>>choice;
                        vector<vehicle>::iterator p;
                        if(sl=='c'){
                            c.erase(c.begin()+choice);

                        }
                        else if(sl=='d')
                            d.erase(d.begin()+choice);
                        cout<<"Vehicle removed from parking slot \n";
                    break;
                }
                case 4:
                	cout<<"Enter C to know the parking status of car slot \n\n"<<"Enter S to know the parking status of Scooter \n\n";
                	char s2;
					cin>>s2;
                	if(s2=='C' || s2=='c')
                	{
                		if(a.size()>=10 && b.size()<10)
						print(b,'B');
						else if(a.size()>=10 && b.size()>=10)
						cout<<"Sorry both the slots for car parking is full \n\n";
						else if(b.size()>=10 && a.size()<10)
						print(a,'A');
						else if(a.size()<10)
						print(a,'a');
						else if(b.size()<10)
						print(b,'b');
				    }
				    if(s2=='S' || s2=='s')
                	{
                		if(c.size()>=10 && d.size()<10)
						print(d,'D');
						else if(d.size()>=10 && c.size()>=10)
						cout<<"Sorry both the slots for scooter parking is full \n\n";
						else if(d.size()>=10 && c.size()<10)
						print(c,'C');
						else if(c.size()<10)
						print(c,'c');
						else if(d.size()<10)
						print(d,'d');
				    }
                	
            break;

                }
cout<<"Enter 1 to continue or any other key to exit \n";
         cin>>q;
            if(q!=1)
            {
                cout<<"Thank You \n\n";
                break;
            }


}while(q==1);
}
