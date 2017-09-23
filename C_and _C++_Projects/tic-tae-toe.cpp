#include<iostream>
#include<cstdlib>
using namespace std;

char s[10] = {'o','1','2','3','4','5','6','7','8','9'};

int check_winner();
void board();
int main()
{
    int player=1,i,ch;
    char mark;
    do
    {
        board();
		player=(player%2)?1:2;

		cout << "Player " << player << ", enter a number:  ";
		cin >> ch;
		mark= (player==1)?'X':'O';
		if (ch == 1 && s[1] == '1')
            s[1] = mark;
        else if(ch==2 && s[2]=='2')
            s[2]=mark;
        else if(ch==3 && s[3]=='3')
            s[3]=mark;
        else if(ch==4 && s[4]=='4')
            s[4]=mark;
        else if(ch==5 && s[5]=='5')
            s[5]=mark;
        else if(ch==6 && s[6]=='6')
            s[6]=mark;
        else if(ch==7 && s[7]=='7')
            s[7]=mark;
        else if(ch==8 && s[8]=='8')
            s[8]=mark;
        else if(ch==9 && s[9]=='9')
            s[9]=mark;

        else
        {
            cout<<"invalid move \n";
            player--;
            cin.ignore();
            cin.get();

        }
        i= check_winner();
        player++;

   }while(i== -1);
   board();
	if(i==1)

		cout<<"==>\aPlayer "<<--player<<" win ";
	else
		cout<<"==>\aGame draw";


    cin.ignore();
    cin.get();
	return 0;
}

// for checking winner

int check_winner()
{
    if(s[1]==s[2]&&s[2]==s[3])
        return 1;
    else if(s[4]==s[5]&&s[5]==s[6])
        return 1;
    else if(s[7]==s[8]&&s[8]==s[9])
        return 1;
    else if(s[1]==s[4]&&s[4]==s[7])
        return 1;
    else if(s[2]==s[5]&&s[5]==s[8])
        return 1;
    else if(s[3]==s[6]&&s[6]==s[9])
        return 1;
    else if(s[1]==s[5]&&s[5]==s[9])
        return 1;
    else if(s[3]==s[5]&&s[5]==s[7])
        return 1;
    else if(s[1]!='1'&&s[2]!='2'&&s[3]!='3'&&s[4]!='4'&&s[5]!='5'&&s[6]!='6'&&s[7]!='7'&&s[8]!='8'&&s[9]!='9')
        return 0;
    else
        return -1;
}

void board()
{
    system("cls");
	cout << "\n\n\tTic Tac Toe\n\n";
	cout << "Player 1 (X)  -  Player 2 (O)" <<"\n"<<"\n";
	cout << endl;
	cout << "     |     |     " << endl;
	cout << "  " << s[1] << "  |  " << s[2] << "  |  " << s[3] << endl;
	cout << "_____|_____|_____" << endl;
	cout << "     |     |     " << endl;

	cout << "  " << s[4] << "  |  " << s[5] << "  |  " << s[6] << endl;
	cout << "_____|_____|_____" << endl;
	cout << "     |     |     " << endl;

	cout << "  " << s[7] << "  |  " << s[8] << "  |  " << s[9] << endl;

	cout << "     |     |     " << endl << endl;


}
