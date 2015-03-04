# This file was *autogenerated* from the file mphase_mms_rans_p2p1_keps.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_1p8 = RealNumber('1.8'); _sage_const_2 = Integer(2); _sage_const_2p1 = RealNumber('2.1'); _sage_const_2p5 = RealNumber('2.5'); _sage_const_0p707106781 = RealNumber('0.707106781'); _sage_const_1p0 = RealNumber('1.0'); _sage_const_1p3 = RealNumber('1.3'); _sage_const_5p2 = RealNumber('5.2'); _sage_const_1p7 = RealNumber('1.7'); _sage_const_0p0 = RealNumber('0.0'); _sage_const_10p0 = RealNumber('10.0'); _sage_const_0p7 = RealNumber('0.7'); _sage_const_0p6 = RealNumber('0.6'); _sage_const_3p7 = RealNumber('3.7')
y = var('y')

def function(phi_0, phi_x, phi_y, phi_xy, 
             f_sin_x, f_cos_x, f_sin_y, f_cos_y, f_sin_xy, f_cos_xy, 
             alpha_x, alpha_y, alpha_xy):
    
    f_0 = phi_0 
    f_x = phi_x*(f_sin_x*sin(alpha_x*x) + f_cos_x*cos(alpha_x*x)) 
    f_y = phi_y*(f_sin_y*sin(alpha_y*y) + f_cos_y*cos(alpha_y*y)) 
    f_xy = phi_xy*(f_sin_xy*sin(alpha_xy*x*y/pi) + f_cos_xy*cos(alpha_xy*x*y/pi)) 
    f = f_0 + f_x + f_y + f_xy
    return f

p = function(-_sage_const_1p0 , _sage_const_1p0 , _sage_const_1p0 , _sage_const_1p0 ,
             _sage_const_1p0 , _sage_const_0p0 , _sage_const_0p0 , _sage_const_1p0 , _sage_const_1p0 , _sage_const_0p0 ,
             _sage_const_1p0 , _sage_const_1p0 , _sage_const_1p0 )
       
#### Phase 1
u = function(_sage_const_2p5 , _sage_const_1p0 , _sage_const_0p6 , _sage_const_0p0 , 
             _sage_const_0p0 , _sage_const_1p0 , _sage_const_1p0 , _sage_const_0p0 , _sage_const_1p0 , _sage_const_0p0 ,
             _sage_const_1p0 , _sage_const_1p0 , _sage_const_1p0 )
v = integral(-diff(u,x),y)  # divergence free
temperature = function(_sage_const_5p2 , -_sage_const_1p8 , -_sage_const_1p3 , _sage_const_3p7 , 
               _sage_const_1p0 , _sage_const_0p0 , _sage_const_0p0 , _sage_const_1p0 , _sage_const_1p0 , _sage_const_0p0 ,
               _sage_const_1p7 , _sage_const_2p1 , _sage_const_1p3 )
rho = _sage_const_10p0 *temperature + _sage_const_10p0 
nu = _sage_const_0p7 
g_x = _sage_const_0p707106781 
g_y = _sage_const_0p707106781 

tau_xx = _sage_const_2 *nu*diff(u,x)            
tau_xy = nu*(diff(u,y) + diff(v,x))
tau_yy = _sage_const_2 *nu*diff(v,y)            
tau_yx = nu*(diff(u,y) + diff(v,x))  

Su = rho*u*diff(u,x) + rho*v*diff(u,y) - diff(tau_xx, x) - diff(tau_xy, y) - rho*g_x + diff(p,x)  
Sv = rho*u*diff(v,x) + rho*v*diff(v,y) - diff(tau_yx, x) - diff(tau_yy, y) - rho*g_y + diff(p,y)  

Stemperature = u*diff(temperature,x) + v*diff(temperature,y) - (_sage_const_1p0 )*(diff(temperature, x, x) + diff(temperature, y, y))

  
print 'from math import sin, cos, tanh, pi'
print ''
print 'def u(X):'
print '    return', str(u).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''
print 'def v(X):'
print '    return', str(v).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print '' 
print 'def p(X):'
print '    return', str(p).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''  
print 'def temperature(X):'
print '    return', str(temperature).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''  
print 'def rho(X):'
print '    return', str(rho).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''  
print 'def forcing_u(X):'
print '    return', str(Su).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''
print 'def forcing_v(X):'
print '    return', str(Sv).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''
print 'def forcing_temperature(X):'
print '    return', str(Stemperature).replace('e^', 'exp').replace('^', '**').replace('000000000000', '').replace('x', 'X[0]').replace('y', 'X[1]')
print ''
print 'def velocity(X):'
print '   return [u(X), v(X)]'
print ''
print 'def forcing_velocity(X):'
print '   return [forcing_u(X), forcing_v(X)]'