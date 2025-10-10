tamanho_arquivo = float(input("Informe o tamamnho do arquivo(em MB): "))
velo_link = float(input("Digite a velocidade da internet: "))

tmp_se = tamanho_arquivo / velo_link

tmp_minu = tmp_se / 60

print (" Tempo aproximado de dowload: ", tmp_minu, "minutos")