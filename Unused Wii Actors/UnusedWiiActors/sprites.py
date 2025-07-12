# Unused Wii Actors
# Custom Miyamoto sprites.py Module
# Sprites Images




from PyQt5 import QtCore, QtGui
Qt = QtCore.Qt


import spritelib as SLib


ImageCache = SLib.ImageCache




class SpriteImage_RotCannon(SLib.SpriteImage_StaticMultiple):  # 177
    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('RotCannon', 'rot_cannon.png')
        SLib.loadIfNotInImageCache('RotCannonU', 'rot_cannon_u.png')


    def dataChanged(self):


        upsideDown = (self.parent.spritedata[5] >> 4) & 1
        if not upsideDown:
            self.image = ImageCache['RotCannon']
            self.offset = (-12, -29)
        else:
            self.image = ImageCache['RotCannonU']
            self.offset = (-12, 0)


        super().dataChanged()




class SpriteImage_RotCannonPipe(SLib.SpriteImage_StaticMultiple):  # 178
    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('RotCannonPipe', 'rot_cannon_pipe.png')
        SLib.loadIfNotInImageCache('RotCannonPipeU', 'rot_cannon_pipe_u.png')


    def dataChanged(self):


        upsideDown = (self.parent.spritedata[5] >> 4) & 1
        if not upsideDown:
            self.image = ImageCache['RotCannonPipe']
            self.offset = (-40, -74)
        else:
            self.image = ImageCache['RotCannonPipeU']
            self.offset = (-40, 0)


        super().dataChanged()




class SpriteImage_CloudBlock(SLib.SpriteImage_Static):  # 189
    def __init__(self, parent):
        super().__init__(
            parent,
            1.5,
            ImageCache['CloudBlock'],
            (-4, -8),
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('CloudBlock', 'cloud_block.png')




class SpriteImage_GlowBlock(SLib.SpriteImage):  # 199
    def __init__(self, parent):
        super().__init__(parent, 1.5)
        self.spritebox.shown = False


        self.aux.append(SLib.AuxiliaryImage(parent, 48, 48))
        self.aux[0].image = ImageCache['GlowBlock']
        self.aux[0].setPos(-12, -12)


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('GlowBlock', 'glow_block.png')




class SpriteImage_PropellerBlock(SLib.SpriteImage_Static):  # 202
    def __init__(self, parent):
        super().__init__(
            parent,
            1.5,
            ImageCache['PropellerBlock'],
            (-3, -6),
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('PropellerBlock', 'propeller_block.png')




class SpriteImage_CubeKinokoRot(SLib.SpriteImage_StaticMultiple):  # 256
    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('CubeKinokoG', 'cube_kinoko_g.png')
        SLib.loadIfNotInImageCache('CubeKinokoR', 'cube_kinoko_r.png')


    def dataChanged(self):


        style = self.parent.spritedata[4] & 1
        if style == 0:
            self.image = ImageCache['CubeKinokoR']
        else:
            self.image = ImageCache['CubeKinokoG']


        super().dataChanged()




class SpriteImage_BigShell(SLib.SpriteImage_StaticMultiple):  # 267
    def __init__(self, parent):
        super().__init__(parent, 1.5)
        self.offset = (-97, -145)


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BigShell', 'bigshell_green.png')
        SLib.loadIfNotInImageCache('BigShellGrass', 'bigshell_green_grass.png')


    def dataChanged(self):
        style = self.parent.spritedata[5] & 1


        if style == 0:
            self.image = ImageCache['BigShellGrass']
        else:
            self.image = ImageCache['BigShell']


        super().dataChanged()




class SpriteImage_PoltergeistItem(SLib.SpriteImage):  # 305
    def __init__(self, parent):
        super().__init__(parent, 1.5)
        self.spritebox.shown = False


        self.aux.append(SLib.AuxiliaryImage(parent, 60, 60))
        self.aux[0].image = ImageCache['PolterQBlock']
        self.aux[0].setPos(-18, -18)
        self.aux[0].hover = False


    @staticmethod
    def loadImages():
        if 'PolterQBlock' in ImageCache: return


        SLib.loadIfNotInImageCache('GhostHouseStand', 'ghost_house_stand.png')


        polterstand = SLib.GetImg('polter_stand.png')
        polterblock = SLib.GetImg('polter_qblock.png')


        standpainter = QtGui.QPainter(polterstand)
        blockpainter = QtGui.QPainter(polterblock)


        standpainter.drawPixmap(18, 18, ImageCache['GhostHouseStand'])
        blockpainter.drawPixmap(18, 18, ImageCache['Blocks'][0])


        del standpainter
        del blockpainter


        ImageCache['PolterStand'] = polterstand
        ImageCache['PolterQBlock'] = polterblock


    def dataChanged(self):


        style = self.parent.spritedata[5] & 15
        if style == 0:
            self.offset = (0, 0)
            self.height = 16
            self.aux[0].setSize(60, 60)
            self.aux[0].image = ImageCache['PolterQBlock']
        else:
            self.offset = (8, -16)
            self.height = 32
            self.aux[0].setSize(60, 84)
            self.aux[0].image = ImageCache['PolterStand']


        self.aux[0].setPos(-18, -18)


        super().dataChanged()




class SpriteImage_GhostHouseStand(SLib.SpriteImage_Static):  # 310
    def __init__(self, parent):
        super().__init__(
            parent,
            1.5,
            ImageCache['GhostHouseStand'],
            (8, -16),
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('GhostHouseStand', 'ghost_house_stand.png')




class SpriteImage_CubeKinokoLine(SLib.SpriteImage_Static):  # 312
    def __init__(self, parent):
        super().__init__(
            parent,
            1.5,
            ImageCache['CubeKinokoP'],
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('CubeKinokoP', 'cube_kinoko_p.png')




class SpriteImage_MoveWhenOnMetalLavaBlock(SLib.SpriteImage_StaticMultiple):  # 319
    @staticmethod
    def loadImages():
        if 'MetalLavaBlock0' in ImageCache: return
        ImageCache['MetalLavaBlock0'] = SLib.GetImg('lava_iron_block_0.png')
        ImageCache['MetalLavaBlock1'] = SLib.GetImg('lava_iron_block_1.png')
        ImageCache['MetalLavaBlock2'] = SLib.GetImg('lava_iron_block_2.png')


    def dataChanged(self):
        size = (self.parent.spritedata[5] & 0xF) % 3
        self.image = ImageCache['MetalLavaBlock%d' % size]


        super().dataChanged()




class SpriteImage_TiltingGirder(SLib.SpriteImage_Static):  # 345
    def __init__(self, parent):
        super().__init__(
            parent,
            1.5,
            ImageCache['TiltingGirder'],
            (0, -18),
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('TiltingGirder', 'tilting_girder.png')




class SpriteImage_RollingHillWith1Pipe(SpriteImage_RollingHillWithPipe):  # 355
    pass




class SpriteImage_BoltPlatform(SLib.SpriteImage):  # 358
    def __init__(self, parent):
        super().__init__(parent, 1.5)
        self.spritebox.shown = False


    @staticmethod
    def loadImages():
        if 'BoltPlatformL' in ImageCache: return
        ImageCache['BoltPlatformL'] = SLib.GetImg('bolt_platform_left.png')
        ImageCache['BoltPlatformM'] = SLib.GetImg('bolt_platform_middle.png')
        ImageCache['BoltPlatformR'] = SLib.GetImg('bolt_platform_right.png')


    def dataChanged(self):
        self.offset = (0, -2)
        super().dataChanged()


        length = self.parent.spritedata[5] & 0xF
        self.width = (length + 2) * 16


    def paint(self, painter):
        super().paint(painter)


        painter.drawPixmap(0, 0, ImageCache['BoltPlatformL'])
        painter.drawTiledPixmap(24, 3, int(self.width * 1.5) - 48, 24, ImageCache['BoltPlatformM'])
        painter.drawPixmap(int(self.width * 1.5) - 24, 0, ImageCache['BoltPlatformR'])




class SpriteImage_BoltPlatformWire(SLib.SpriteImage_Static):  # 360
    def __init__(self, parent):
        super().__init__(
            parent,
            1.5,
            ImageCache['BoltPlatformWire'],
            (5, -240),
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('BoltPlatformWire', 'bolt_platform_wire.png')




class SpriteImage_SilverGearBlock(SLib.SpriteImage_StaticMultiple):  # 376
    @staticmethod
    def loadImages():
        if 'SilverGearBlockDown3' in ImageCache: return
        for gear in range(4):
            image = SLib.GetImg('silver_gear_block_%d.png' % gear, True)
            ImageCache['SilverGearBlockUp%d' % gear] = QtGui.QPixmap.fromImage(image)
            ImageCache['SilverGearBlockDown%d' % gear] = QtGui.QPixmap.fromImage(image.mirrored(True, True))


    def dataChanged(self):
        style = self.parent.spritedata[5] & 3
        flipped = (self.parent.spritedata[5] >> 4) & 1


        if flipped:
            self.image = ImageCache['SilverGearBlockDown%d' % style]
        else:
            self.image = ImageCache['SilverGearBlockUp%d' % style]


        super().dataChanged()




class SpriteImage_MovingGemBlock(SLib.SpriteImage_Static):  # 377
    def __init__(self, parent):
        super().__init__(
            parent,
            1.5,
            ImageCache['MovingGemBlock'],
        )


        self.aux.append(SLib.AuxiliaryTrackObject(parent, 16, 16, SLib.AuxiliaryTrackObject.Vertical))


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('MovingGemBlock', 'moving_gem_block.png')


    def dataChanged(self):
        direction = self.parent.spritedata[2] & 1
        distance = (self.parent.spritedata[4] & 0xF0) >> 4


        self.aux[0].setSize(16, (distance * 16) + 16)
        if direction == 0: # up
            self.aux[0].setPos(self.width / 2, -distance * 24)
        else: # down
            self.aux[0].setPos(self.width / 2, self.height - 8)


        super().dataChanged()




class SpriteImage_FloatingBarrel(SLib.SpriteImage_Static):  # 522
    def __init__(self, parent):
        super().__init__(
            parent,
            1.5,
            offset = (-16, -9)
        )


        img = ImageCache['FloatingBarrel']
        self.width = (img.width() / self.scale) + 1
        self.height = (img.height() / self.scale) + 2


        self.aux.append(SLib.AuxiliaryImage(parent, img.width(), img.height()))
        self.aux[0].image = img


        path = QtGui.QPainterPath()
        path.lineTo(QtCore.QPointF(self.width * 1.5, 0))


        self.aux.append(SLib.AuxiliaryPainterPath(parent, path, img.width(),
            SLib.OutlinePen.width(), 0, 36))


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('FloatingBarrel', 'barrel_floating.png')


    def dataChanged(self):
        # Don't let SLib.SpriteImage_Static reset size
        SLib.SpriteImage.dataChanged(self)




class SpriteImage_Crow(SLib.SpriteImage_Static):  # 529
    def __init__(self, parent):
        super().__init__(
            parent,
            1.5,
            ImageCache['Crow'],
            (-3, -2),
        )


    @staticmethod
    def loadImages():
        SLib.loadIfNotInImageCache('Crow', 'crow.png')






ImageClasses = {
    177: SpriteImage_RotCannon,
    178: SpriteImage_RotCannonPipe,
    189: SpriteImage_CloudBlock,
    199: SpriteImage_GlowBlock,
    202: SpriteImage_PropellerBlock,
    256: SpriteImage_CubeKinokoRot,
    267: SpriteImage_BigShell,
    305: SpriteImage_PoltergeistItem,
    310: SpriteImage_GhostHouseStand,
    312: SpriteImage_CubeKinokoLine,
    319: SpriteImage_MoveWhenOnMetalLavaBlock,
    345: SpriteImage_TiltingGirder,
    355: SpriteImage_RollingHillWith1Pipe,
    358: SpriteImage_BoltPlatform,
    360: SpriteImage_BoltPlatformWire,
    376: SpriteImage_SilverGearBlock,
    377: SpriteImage_MovingGemBlock,
    522: SpriteImage_FloatingBarrel,
    529: SpriteImage_Crow,
}