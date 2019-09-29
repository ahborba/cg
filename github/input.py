from transformacao import *


class input:

   def transformacao_bezier(self, op, mat, dx, dy, dados):
        if op == 'rotacao' or op == 'escala':
            dX = self.pontos['fundo_preto'][0][0]
            dY = self.pontos['fundo_preto'][0][1]

        nova_mat = []
        for linha in mat:
            if op == 'translacao':
                nova_mat.append(self.transf.translacao(linha, dx, dy))
            elif op == 'escala':
                nova_mat.append(self.transf.escala(linha, dx, dy, dX, dY))
            elif op == 'rotacao':
                nova_mat.append(self.transf.rotacao(linha, dX, dY))
        return nova_mat

    def transformacao_lin(self,op,linha,dx,dy,dados):
        if op =='rotacao' or op=='escala':
            dX = self.pontos['fundo_preto'][0][0] 
            dY = self.pontos['fundo_preto'][0][1]


        if op =='translacao':
            return self.transf.translacao(linha,dx,dy)
        elif op =='escala':
            return self.transf.escala(linha,dx,dy,dX,dY)
        else:
            return self.transf.rotacao(linha,dX,dY)
        

    def transformacao_letras(self,op,dx=0,dy=0):
        if op =='rotacao' or op=='escala':
            dX = self.pontos['fundo_preto'][0][0] 
            dY = self.pontos['fundo_preto'][0][1]
        self.pontos['g']=self.transformacao_lin(op,self.pontos['g'],dx,dy,'g')
        self.pontos['i']=self.transformacao_bezier(op,self.pontos['i'],dx,dy,'i')
        self.pontos['t']=self.transformacao_bezier(op,self.pontos['t'],dx,dy,'t')
        self.pontos['h']=self.transformacao_bezier(op,self.pontos['h'],dx,dy,'h')
        self.pontos['u']=self.transformacao_lin(op,self.pontos['u'],dx,dy,'u')
        self.pontos['b']=self.transformacao_lin(op,self.pontos['b'],dx,dy,'b')
