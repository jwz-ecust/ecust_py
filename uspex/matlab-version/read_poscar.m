% this function is usedt ot read POSCAR files .
% input is the input file's name .
function [coor,LATT,numIons,natom,atom_chan] = read_poscar(input)
[fid,message] = fopen(input);

tmp = fgetl(fid) ;    % tile .
factor = str2num(fgetl(fid)) ; % the zoom factor .

LATT =zeros(3);    % the bulk LATTIC£®
for i =1 : 3
    tmp = fgetl(fid);
    LATT(i,:) = str2num(tmp);
end
LATT = LATT*factor;

% atom type
tmp = fgetl(fid);
ntyp = str2num(tmp); % number of each type atom .
numIons = ntyp;

if isempty(ntyp)
    tmp= fgetl(fid);
    ntyp = str2num(tmp);
    numIons = ntyp;
end
% direct
natom = sum(ntyp);
tmp = fgetl(fid);  % the line is the string 'Direct'
if findstr(tmp,'S')
	tmp = fgetl(fid);
end

coor = zeros(natom,3);   %¡¡atom 's coordination .
atom_chan = zeros(natom,3);  % the atom fix or not , if atom_chan(ii,1) ==1 , it means that the x dirction is not fix .

for ii = 1 : natom
    tmp=fgetl(fid);
    temp = regexp(tmp,'\s+','split');
    if isempty(temp{1})
        temp=temp(2:end);
    end
    for jj = 1 : 3
        coor(ii,jj)=str2num(temp{jj});
        try
            if temp{jj+3} == 'T'
                atom_chan(ii,jj) = 1;
            else
                atom_chan(ii,jj) = 0 ;
            end
        catch
        end
    end
end
fclose(fid);
end
