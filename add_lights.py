"""
Script UE Editor Python - Aggiunge luci al loft MetaUdemy
Esegui dall'Output Log: py "C:/Users/User/Udemy/MetaUdmy/add_lights.py"
"""
import unreal

def spawn_point_light(label, x, y, z, intensity, temperature, indirect=4.0, radius=500.0):
    loc = unreal.Vector(x, y, z)
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.PointLight, loc)
    if not actor:
        print(f"ERRORE: impossibile creare {label}")
        return None
    actor.set_actor_label(label)
    comp = actor.get_component_by_class(unreal.PointLightComponent)
    comp.set_editor_property('intensity', float(intensity))
    comp.set_editor_property('use_temperature', True)
    comp.set_editor_property('temperature', float(temperature))
    comp.set_editor_property('indirect_lighting_intensity', float(indirect))
    comp.set_editor_property('attenuation_radius', float(radius))
    comp.set_editor_property('mobility', unreal.ComponentMobility.STATIC)
    print(f"OK: {label} @ ({x}, {y}, {z})")
    return actor

def spawn_spot_light(label, x, y, z, pitch, yaw, intensity, temperature, outer_angle=60.0, indirect=4.0):
    loc = unreal.Vector(x, y, z)
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.SpotLight, loc)
    if not actor:
        print(f"ERRORE: impossibile creare {label}")
        return None
    actor.set_actor_label(label)
    actor.set_actor_rotation(unreal.Rotator(pitch, yaw, 0), False)
    comp = actor.get_component_by_class(unreal.SpotLightComponent)
    comp.set_editor_property('intensity', float(intensity))
    comp.set_editor_property('use_temperature', True)
    comp.set_editor_property('temperature', float(temperature))
    comp.set_editor_property('outer_cone_angle', float(outer_angle))
    comp.set_editor_property('indirect_lighting_intensity', float(indirect))
    comp.set_editor_property('mobility', unreal.ComponentMobility.STATIC)
    print(f"OK: {label} @ ({x}, {y}, {z})")
    return actor

print("=== Aggiunta luci loft MetaUdemy ===")

# --- LIVING ROOM (ceiling lamps @ Z=230, warm 3000K) ---
spawn_point_light("Light_Living_01", -150, 176, 230, 800, 3000, radius=400)
spawn_point_light("Light_Living_02", -270, 176, 230, 800, 3000, radius=400)
spawn_point_light("Light_Living_03", -390, 176, 230, 800, 3000, radius=400)

# --- FLOOR LAMP (living room corner, very warm) ---
spawn_point_light("Light_FloorLamp", -412, 570, 80, 300, 2700, radius=300)

# --- PENDANTS sopra tavolo pranzo ---
spawn_point_light("Light_Pendant_01", -168, -356, 215, 250, 2700, radius=250)
spawn_point_light("Light_Pendant_02",  -39, -356, 215, 250, 2700, radius=250)

# --- CUCINA (cool white 6000K) ---
spawn_point_light("Light_Kitchen_01", -250,  -90, 200, 600, 6000, radius=350)
spawn_point_light("Light_Kitchen_02", -300,  175, 200, 600, 6000, radius=350)

# --- BAGNO (spotlights puntati verso il basso, pitch=-90) ---
spawn_spot_light("Light_Bath_01", -128, -321, 230, -90, 0, 250, 6000, outer_angle=55)
spawn_spot_light("Light_Bath_02", -218, -321, 230, -90, 0, 250, 6000, outer_angle=55)
spawn_spot_light("Light_Bath_03", -268, -321, 230, -90, 0, 250, 6000, outer_angle=55)
spawn_spot_light("Light_Bath_04", -358, -321, 230, -90, 0, 250, 6000, outer_angle=55)
spawn_spot_light("Light_Bath_05", -128, -196, 230, -90, 0, 250, 6000, outer_angle=55)
spawn_spot_light("Light_Bath_06", -218, -196, 230, -90, 0, 250, 6000, outer_angle=55)

# --- INGRESSO ---
spawn_spot_light("Light_Entrance_01",  50, -170, 240, -90, 0, 400, 4500, outer_angle=65)
spawn_spot_light("Light_Entrance_02", -78, -170, 240, -90, 0, 400, 4500, outer_angle=65)

# --- CAMERA DA LETTO (mezzanine, Z~390) ---
spawn_point_light("Light_Bedroom_01",  54, -339, 390, 500, 2800, radius=400)
spawn_point_light("Light_Bedroom_02", -233, -339, 390, 500, 2800, radius=400)

# --- FILL LIGHT soggiorno (luce morbida diffusa) ---
spawn_point_light("Light_Living_Fill", -95, 400, 180, 200, 5000, indirect=6.0, radius=600)

# --- LUCE SCALA mezzanino ---
spawn_point_light("Light_Stair", 200, 236, 200, 300, 4000, radius=400)

print("=== Completato! Ora fai Build Lighting. ===")
