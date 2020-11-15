#Question 5. Consider two square num py arrays. Stack them vertically and horizontally.

a = np.array([[11, 24],

[36, 47]])

b = np.array([[51, 62],

[70, 86]])

print("Vertical stacking: \n", np.vst print("\nHorizontal stacking: \n", np

ack((a, b)))

.hstack((a, b)))

Vertical stacking:

[[11 24]

[36 47]

[51 62]

[70 86]1

Horizontal stacking:

[[11 24 51 62] [36 47 70 86]]

