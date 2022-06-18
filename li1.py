a = [['hii', 4, 'hello', 8],
	['km chho', 3, 5, 7 ],
	[ 8, 6, 4, 2 ],
	[ 7, 5, 3, 'majama' ]
]

for i in range(len(a)):
    for j in range(len(a[i])):
        print([a[i][j]], end=" ")
    print()