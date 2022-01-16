# This model will use regression to predict shelter capacity on any given day

using CSV, Downloads
using DataFrames

#------------------------------------------------------|
# CSV formating and DataFrame creation

function fix_dates(df) 
	# inplace function
	dates = [31,28,31,30,31,30,31,31,30,31,30,31] #dates in each month (not including leap years)

	# creates dataframe with int values for month and date
	fixed = DataFrame([(Month=parse(Int8,a),Day=parse(Int8,b),Year=parse(Int32,split(c," ")[1])) 
			   for (a,b,c) in [split(df[i,1],"/") for i in 1:length(df.Date)]])

	# creates array of fixed dates (i.e int between 1-365)
	col = [sum(dates[1:fixed.Month[i]-1])+fixed[i,2] for i in 1:length(fixed.Month)]

	insertcols!(df,1,:Day => col) 
end

#------------------------------------------------------|
# ML Model section

mutable struct Regressor
	X::Matrix{Float64};
	Y::Vector{Float64};
	w::Vector{Float64}; 
	stepsize::Float64;
	gradient::Float64;
end

function basis(pr::Regressor,p::Int64)
	# linearizes X, creates features
	# p is polynomial degree
	return 0;
end

function mb_update(pr::Regressor,batch_size::Int64,epochs::Int64)
	# mini-batch gradient descent to update param w
	
	# using this to sample x,y pairs randomly
	indices = randperm!(1:length(pr.X));

	for p in 1:epochs
		for k in ((p*batch_size)-batch_size):(p*batch_size)
			pr.gradient = ((pr.X[k,:]*pr.w[k]) - pr.Y[k])*self.X[k,:];
			pr.stepsize = (1/p+1);
			pr.w = pr.w - (pr.stepsize*pr.gradient)
		end
	end

end

#------------------------------------------------------|

# running functions here
shelters_csv = "edmonton_shelters.csv";

# creating dataframes
# copy is to prevent screwing up original dataframe
shelters_static = DataFrame(CSV.File(shelters_csv));
shelters_copy = copy(shelters_static);

# need to change dates to int values
dropmissing!(shelters_copy,[:Overnight,:Capacity]);
fix_dates(shelters_copy);

# making column overnight/capacity
shelters_copy = transform(shelters_copy, [:Overnight,:Capacity] => (./) => :Ratio);

# formatting the dataframe, removing columns that aren't used
remove_col = [:Date,Symbol("Shelter Type"),:Shelter,:Year,:Month,:Organization,:City,:Capacity,:Overnight,:Funded];
select!(shelters_copy,Not(remove_col));

# dataframe of shelter names + frequency
shelter_names = combine(groupby(shelters_copy,"Shelter Name"), nrow  => :count);

# writing dataframe to csv
CSV.write("fixed.csv",shelters_copy)

#-----------------------------------------------------|
