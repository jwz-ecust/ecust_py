function [Matrix,myBasic,mySite] = ExtractCoefficient(Reactions,Rline)
Sbasic = '#';
mySite = [];
myBasic = [];
temp = char(Reactions)';
temp = temp(:)';
t  = isempty(strfind(temp,[Sbasic '1'])) & strfind(temp,Sbasic);
if sum(t)
    mySite{1} = Sbasic;
end
for ix = 1:length(Reactions)
    a = Reactions{ix};    
    pofArrows(ix) = strfind(a,'<->');
    a = strrep(a,'<->','+');
    alist = regexp(a,'+','split');
    list{ix} = alist;
    Ns = length(mySite);
    for ik = 1:Ns
        alist = strrep(alist,mySite{ik},'');   
    end 
    for il = 1:length(alist)
        alist = strrep(alist,'(p)','');
        alist = strrep(alist,'(c)','');       
        if strfind(alist{il},Sbasic)
            Ns = length(mySite);
            mySite{Ns + 1} = [Sbasic num2str(Ns + 1)];
            alist = strrep(alist,mySite{Ns + 1},'');
        end
        if ~isempty(alist{il}) && ~isvarname(alist{il})
            disp([char(10) 'Find Illegal Variable As Name Of Species : ' alist{il} ' at line ' num2str(Rline(ix))]);
            diary off;
            quit;
        end
    end
    for jx = 1:length(alist)
        if ~isempty(alist{jx})
            strIsfound = mystrMatch(myBasic,alist(jx));
        else
            continue;
        end
        if strIsfound == 0
            myBasic{length(myBasic)+1} = alist{jx};
        end
    end
end
Ns = length(mySite);
myBasic = sort(myBasic);
Matrix =  zeros(length(list),length(myBasic) + Ns,Ns + 2);
for ix = 1:length(list)
    mark = 0;
    for jx = 1:length(list{ix})
        alist = list{ix};
        mark = mark + length(alist{jx}) + 1;
        if (mark <= pofArrows(ix))
            sign = -1;
        else
            sign = 1;
        end
        psite0 = mystrMatch(myBasic,alist(jx)) + mystrMatch(strcat(myBasic,'(p)'),alist(jx));
        if psite0
            Matrix(ix,psite0,end) = Matrix(ix,psite0,end) + sign;
            continue;
        end
        psite1 =  mystrMatch(strcat(myBasic,'(c)'),alist(jx));
        if psite1
            Matrix(ix,psite1,end -1 ) = Matrix(ix,psite1,end - 1) + sign;
            continue;
        end
        for kx = 1:Ns
            psitea = mystrMatch(strcat(myBasic,mySite(kx)),alist(jx));
            if psitea
                Matrix(ix,psitea,kx) = Matrix(ix,psitea,kx) + sign;
                break;
            end
        end
        psites = mystrMatch(mySite,alist(jx));
        if psites
            Matrix(ix,end - Ns + psites,psites) = Matrix(ix,end - Ns + psites,psites) + sign;
        end

    end
end










function [strIsfound] = mystrMatch(mystring,searchstring)
strIsfound = 0;
for ix = 1:length(mystring)
    if strcmp(mystring(ix),searchstring)
        strIsfound = ix;
        break;
    end
end


