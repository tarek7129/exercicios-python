notas = [input(),input(),input(),input()]

media = float(notas[0])*2 + float(notas[1])*3 + float(notas[2])*4 + float(notas[3])*1
media = media/10

print(f'Media: {media:.1f}')
if media >= 7 :
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else :
    print("Aluno em exame.")
    nota5 = (input())
    media = media + float(nota5)
    print(f'Nota do exame: {nota5}')
    media = media/2
    if media >= 5:
        print("Aluno aprovado.")
    else :
        print("Aluno reprovado.")
    print(f'Media final: {media:.1f}')