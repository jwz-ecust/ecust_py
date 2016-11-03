function get_xtl(varargin)
%filename_new=inputfilename;
%space=findstr(atomtype,' ');
%len_atomtype= length(atompype)
%if nargin < 2, error('Not enough input parameter'); end
msg = nargchk(2,Inf,nargin);
error(msg);
inputfilename=varargin{1};
for kk= 1 : nargin -1
  type_atom{kk} = varargin{kk+1};
end
%% get the number of the POSCAR files
fp = fopen(inputfilename,'r');
ttt= fgetl(fp);
POSCAR_num = 0;  % the POSCAR file number
while ttt ~=-1
    if findstr(ttt,'Direct');
        POSCAR_num = POSCAR_num + 1;
    end
    ttt = fgetl ( fp );

end
fclose(fp);
%%
fid=fopen(inputfilename,'r');

temp=fgetl( fid );
gen=1;
while temp ~= -1
  %  gen=1;         %����
     aaa=findstr(temp,' ');
     if aaa
         filename_new=[temp(1:aaa(1)) '_generation_' num2str(gen) '.xtl'];
     else
         filename_new=[temp '_generation_' num2str(gen) '.xtl'];
     end
     temp=fgetl(fid);     % �Ŵ�ϵ��
     factor=str2num(temp);
     LATT=zeros(3);
     for ii=1:3
         line=fgetl(fid);
         LATT(ii,:)=str2num(line);
     end
     Bulk_lat=LATT*factor;

     temp=fgetl(fid);
     ntype=str2num(temp);  % ÿ��ԭ�ӵĸ���
     if isempty(ntype)
         tmp=fgetl(fid);
         ntype = str2num(tmp);
     end
     natom=sum(ntype);     % ԭ�ӵ�����
     temp=fgetl(fid);         %  the direct
     Sel_POS = findstr(temp, 'S'); % ��û�� Sel �ֶ�

     if Sel_POS    %�������С���wel ' , �ٶ�һ�� ��
         temp = fgetl ( fid );
     end
     for ll = 1 : natom
         temp=fgetl(fid);
         D_position = findstr( temp ,'.'); % С��������λ��
         for kp = 1 : length( D_position ) % С��������
             D_p = D_position( kp );
             string_temp= temp( D_p-2 : D_p + 6);
             coordinates ( ll , kp ) = str2num(string_temp);
         end
         %coordinates = fscanf(fid,'%g',[3,natom]);
         %coordinates = coordinates' ;
     end
  %   temp=fgetl(fid);  % �����ļ���ͷ
     fp=fopen(filename_new,'w');
     fprintf(fp,['TITLE   ' filename_new ' \n']);
     fprintf(fp,'CELL\n');
     lat_abc=latConverter(Bulk_lat);       % ��������
     lat_abc(4)=lat_abc(4)*180/3.1416;
     lat_abc(5)=lat_abc(5)*180/3.1416;
     lat_abc(6)=lat_abc(6)*180/pi;
     fprintf(fp,'%-12.6f\t%-12.6f\t%-12.6f\t%-12.6f\t%-12.6f \t%-12.6f\n', lat_abc);
     fprintf(fp,'SYMMERY  NUMBER  1\n');
     fprintf(fp,'SYMMETRY  LABEL  P1\n');
     fprintf(fp,'ATOMS\n');
     fprintf(fp,'%-12.6s\t%-12.6s\t%-12.6s\t%-12.6s\n','NAME','X','Y','Z');
     for jj= 1 : length( ntype );
         nu_be = sum( ntype(1 : jj-1 ));
         for ii = 1 : ntype( jj )
             fprintf( fp ,  '%-12.6s\t', type_atom{jj});
             fprintf( fp ,  '%-12.6f\t%-12.6f\t%-12.6f\n' , coordinates( nu_be + ii , :));
         end
     end
         fprintf(fp,'EOF\n');
         fclose(fp);
         gen = gen +1;
         if gen > POSCAR_num; % if gen > POSCAR_num this mean that we have get all the POSCAR files
             break;
         end
         temp = fgetl(fid);

end
end


function output = latConverter(input)
if size(input,1) ==3
    output = zeros(6,1);
    output(1,1) = sqrt(sum(input(1,:).^2));     % a
    output(2,1) = sqrt(sum(input(2,:).^2));     % b
    output(3,1) = sqrt(sum(input(3,:).^2));     % c
    output(6,1) = acos(sum(input(1,:).*input(2,:))/(output(1,1)*output(2,1)));   % jiaodu 1
    output(5,1) = acos(sum(input(1,:).*input(3,:))/(output(1,1)*output(3,1)));   % jiaodu 2
    output(4,1) = acos(sum(input(2,:).*input(3,:))/(output(2,1)*output(3,1)));   % jiaodu 3
else
    output = zeros(3);
    output(1,1) = input(1);
    output(2,1) = input(2)*cos(input(6));
    output(2,2) = input(2)*sin(input(6));
    output(3,1) = input(3)*cos(input(5));
    output(3,2) = input(3)*cos(input(4))*sin(input(6))-((input(3)*cos(input(5))-input(3)*cos(input(4))*cos(input(6)))/tan(input(6)));
    output(3,3) = sqrt(input(3)^2 -output(3,1)^2 - output(3,2)^2);
end
if ~isreal(output)
    du =1;
end

end
