#transformation for a complex number
import cmath
import matplotlib.pyplot as plt

def t(z):    
    rc=float(input("Enter real part of translation vector:"))
    ic=float(input("Enter imaginary part of translation vector:"))
    c=complex(rc,ic)
    zc=z+c    
    k=float(input("Enter scale factor:"))
    zk=z*k
    A=float(input("Enter rotation angle in degrees:"))
    rad=cmath.pi*A/180
    rot_factor = cmath.rect(1,rad) # Creates a complex number with magnitude 1 and phase angle
    zr = z * rot_factor
    choice=input("Choose reflection axis(R for Real axis & I for imaginary axis):")
    if choice=='R':
        z_ref = z.conjugate()
        ref_label = f'Reflected Real={z_ref:.2f}'
    elif choice == 'I':
        z_ref = -z.conjugate()
        ref_label = f'Reflected Imaginary={z_ref:.2f}'
    else:
        print("Invalid choice. Defaulting to Real Axis.") #in case anything other than R or I is written
        z_ref = z.conjugate()
        ref_label = f'Reflected Real={z_ref:.2f}'
    plt.figure()
    plt.axhline(0,color='black')
    plt.axvline(0,color='black')
    plt.quiver(0,0,z.real,z.imag,angles ='xy', scale_units='xy',scale=1,label=f'z={z}',width=0.003)
    plt.quiver(0,0,zc.real,zc.imag,angles='xy',scale_units='xy',scale=1,label=f'Translated={zc.real:.2f}{zc.imag:+.2f}j',color='green',width=0.002) #translation
    plt.quiver(0,0,zk.real,zk.imag,angles='xy',scale_units='xy',scale=1,label=f'Scaled={zk.real:.2f}{zk.imag:+.2f}j',color='red',width=0.0026) #scaling
    plt.quiver(0,0,zr.real,zr.imag,angles='xy',scale_units='xy',scale=1,label=f'Rotated={zr.real:.2f}{zr.imag:+.2f}j',color='blue',width=0.002) #rotation
    plt.quiver(0,0,z_ref.real,z_ref.imag,angles='xy',scale_units='xy',scale=1,label=ref_label,color='orange',width=0.002) #reflection

    x_coords = [0, z.real, zc.real, zk.real, zr.real, z_ref.real]
    y_coords = [0, z.imag, zc.imag, zk.imag, zr.imag, z_ref.imag]    
    plt.xlim(min(x_coords)-2,max(x_coords)+3)
    plt.ylim(min(y_coords)-2,max(y_coords)+3)
    plt.gca().set_aspect=('equal')
    plt.title("Transformation of complex number")
    plt.legend(fontsize=8, loc='upper left')
    plt.grid(True,linestyle='--')
    plt.show()
while True:
    print("\n--- Complex Number Transformation ---")
    rz = float(input("Enter real part of z: "))
    iz = float(input("Enter imaginary part of z: "))
    z = complex(rz, iz)
    t(z)
    again = input("Run again? (Y/N): ").upper()
    
    if again != 'Y':
        print("Program ended :)")
        break

    
    
    
    
    
