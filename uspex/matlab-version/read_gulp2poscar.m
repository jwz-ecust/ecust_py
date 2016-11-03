% ���������ڶ�ȡgulp.gin�ļ��õ�POSCAR�ļ�
%varargin{1}Ϊ�����ļ�����varargin{2 ...} Ϊ����Ԫ�ص��������
function read_gulp2poscar(varargin)

msg = nargchk(2,Inf,nargin);
error(msg);
inputfile = varargin{1};
atomtype=varargin(2:end); % Ԫ������ķ���
n_type = length(atomtype); % Ԫ������ĸ���
numIons = zeros( n_type,1); % ÿ��Ԫ�ظ���
coor = cell(1,n_type);      % Ԫ�����꼰 �Ƿ���xyz����䶯

fid = fopen ( inputfile ,'r'); 
temp = fgetl(fid);
needcell = 1;
running = 1 ;
while running
    if temp == -1 % �ļ�ĩβ
        break;
    end
    %% get the cell
    if findstr(temp,'cell')
        if needcell
            needcell = 0;
            temp = fgetl(fid);
            d = find( double(temp) == 0 );
            temp(d) = [];
            lattice = sscanf (temp ,'%g %g %g %g %g %g',[6,1]);
            lattice(4:6) = lattice(4:6)*pi/180;
            lattice = latConverter(lattice);  % ��ʸ����
        end
            
    end
    %% get fractional
    if findstr(temp,'fractional')
        temp = fgetl(fid) ;
        while ~isempty(temp)
            if findstr ( temp ,'Species')
                running = 0;
                break;
            end
            if findstr(temp,'core') % �� 'core' �ֶ�
                d = find ( double(temp) == 0 );
                temp(d) = [];
                for ii =1 : n_type
                    if findstr(temp,atomtype{ii})
                        coor{ii}(end+1,:) = sscanf(temp,'%*s %*s %g %g %g %*g %*g %*g %g %g %g',[1,6]);
                        numIons(ii) = numIons(ii)+1;       
                    end
                end
            end
            temp = fgetl(fid) ;
            if isempty(temp)
                running = 0;
            end
            
        end
    end
    temp = fgetl(fid);
end
fclose(fid);
%% write POSCAR
fp = fopen('POSCAR','w');
fprintf(fp,'Wenjian_POSCAR\n');
fprintf(fp,'1.000000\n');
for latticeloop = 1 : 3
    fprintf(fp,'%12.6f %12.6f %12.6f\n',lattice(latticeloop , :));
end

for ii = 1 : n_type   % ԭ������
    fprintf(fp,'%6s',atomtype{ii});
end
fprintf(fp,'\n');
for ii = 1 : n_type
    fprintf(fp,'%6d',numIons(ii)); % ÿ��Ԫ�صĸ���
end
fprintf(fp,'\n');
fprintf(fp,'S\n');
fprintf(fp,'Direct\n');
for ii = 1 : n_type
    for jj = 1 : numIons(ii)
        fprintf(fp,'%12.6f %12.6f %12.6f \t',coor{ii}(jj,1:3));
        for kk = 1 : 3
            if coor{ii}(jj,kk+3) == 1.0
                fprintf(fp,'%4s\t','T');
            else
                fprintf(fp,'%4s\t','F');
            end
        end
        fprintf(fp,'\n');
    end    
end
fclose(fp);

end
%%
% this funcion is used to converter lattice , get cell parameters

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
