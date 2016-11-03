% this function is used to get the substrate POSCAR file .
% filename is the input structrue's POSCAR files .
% through this function we can get the SUBSTRATE POSCAR¡¡files .named
% POSCAR_SUBSTRATE
% substrate_thicckness is the substrate' thickness .
% varargin is the type of each atom .
function get_substrate(filename,varargin)
% read the POSCAR files , get the coordinate , Lattice , atom_chan
% atom_chan(i,:) == [1 1 1] ,this means that the atom's x,y,z fraction is
% not fixed .
[coor,LATT,numIons,atom_chan] = read_poscar(filename);
coor = coor - floor(coor);
coor = coor*LATT;              % the fractional coordinate  to cartesian coordinate .
LATT = latConverter(LATT);    % the a,b,c alfa beta gama .
ma = max(coor);                % the max number .
mi = min(coor);                % the min number .
new_Z_length = ma(3)-mi(3) + 0.1 ;
bulk_lat = LATT;
bulk_lat(3) = new_Z_length ;  % correct the Z fractional .
bulk_lat = latConverter(bulk_lat);
coor(:,3) = coor(:,3) - mi(3);
new_coor = coor/bulk_lat;            % get the new atom coordinate .
% write POSCAR??files , named POSCAR_SUBSTRATE
fid = fopen('POSCAR_SUBSTRATE','w');
fprintf(fid,'POSCAR_SUBSTRATE_USPEX\n');
fprintf(fid,'1.000000\n');
for latticeloop = 1:3
    fprintf(fid,'%12.6f %12.6f %12.6f\n',bulk_lat(latticeloop,:));
end
for ii = 1 : length(varargin)         % the number of atom type 
    fprintf(fid,'%6s',varargin{ii});  % the  type of each type atom 
end
fprintf(fid,'\n');
for ii =1 : length(varargin)
    fprintf(fid,'%6d',numIons(ii));      % the number of each type atom .
end
fprintf(fid,'\n');
fprintf(fid,'Direct\n'); % the Dircet line 
for ii = 1 :size(new_coor,1)
    fprintf(fid,'%12.6f %12.6f %12.6f\n',new_coor(ii,:));
end

fclose(fid);
end
