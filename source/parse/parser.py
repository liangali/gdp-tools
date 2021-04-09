from bitstring import BitArray, BitStream

# MFX_PIPE_MODE_SELECT_CMD
cmd = '70000003, 00020100, 00000000, 00000000, 00000000'


# struct
# {
    # uint32_t                 StandardSelect                                   : __CODEGEN_BITFIELD( 0,  3)    ; //!< STANDARD_SELECT
    # uint32_t                 CodecSelect                                      : __CODEGEN_BITFIELD( 4,  4)    ; //!< CODEC_SELECT
    # uint32_t                 StitchMode                                       : __CODEGEN_BITFIELD( 5,  5)    ; //!< STITCH_MODE
    # uint32_t                 FrameStatisticsStreamoutEnable                   : __CODEGEN_BITFIELD( 6,  6)    ; //!< FRAME_STATISTICS_STREAMOUT_ENABLE
    # uint32_t                 ScaledSurfaceEnable                              : __CODEGEN_BITFIELD( 7,  7)    ; //!< SCALED_SURFACE_ENABLE
    # uint32_t                 PreDeblockingOutputEnablePredeblockoutenable     : __CODEGEN_BITFIELD( 8,  8)    ; //!< PRE_DEBLOCKING_OUTPUT_ENABLE_PREDEBLOCKOUTENABLE
    # uint32_t                 PostDeblockingOutputEnablePostdeblockoutenable   : __CODEGEN_BITFIELD( 9,  9)    ; //!< POST_DEBLOCKING_OUTPUT_ENABLE_POSTDEBLOCKOUTENABLE
    # uint32_t                 StreamOutEnable                                  : __CODEGEN_BITFIELD(10, 10)    ; //!< STREAM_OUT_ENABLE
    # uint32_t                 PicErrorStatusReportEnable                       : __CODEGEN_BITFIELD(11, 11)    ; //!< PIC_ERRORSTATUS_REPORT_ENABLE
    # uint32_t                 DeblockerStreamOutEnable                         : __CODEGEN_BITFIELD(12, 12)    ; //!< DEBLOCKER_STREAM_OUT_ENABLE
    # uint32_t                 VdencMode                                        : __CODEGEN_BITFIELD(13, 13)    ; //!< VDENC_MODE
    # uint32_t                 StandaloneVdencModeEnable                        : __CODEGEN_BITFIELD(14, 14)    ; //!< STANDALONE_VDENC_MODE_ENABLE
    # uint32_t                 DecoderModeSelect                                : __CODEGEN_BITFIELD(15, 16)    ; //!< DECODER_MODE_SELECT
    # uint32_t                 DecoderShortFormatMode                           : __CODEGEN_BITFIELD(17, 17)    ; //!< DECODER_SHORT_FORMAT_MODE
    # uint32_t                 ExtendedStreamOutEnable                          : __CODEGEN_BITFIELD(18, 18)    ; //!< Extended stream out enable
    # uint32_t                 Reserved51                                       : __CODEGEN_BITFIELD(19, 31)    ; //!< Reserved
# };

a = BitArray(uintle=0x00020100, length=32)
StandardSelect = a[0:4]
CodecSelect = a[4:5]
StitchMode = a[5:6]
FrameStatisticsStreamoutEnable = a[6:7]
ScaledSurfaceEnable = a[7:8]
PreDeblockingOutputEnablePredeblockoutenable = a[8:9]
PostDeblockingOutputEnablePostdeblockoutenable = a[9:10]
StreamOutEnable = a[10:11]
PicErrorStatusReportEnable = a[11:12]
DeblockerStreamOutEnable = a[12:13]
VdencMode = a[13:14]
StandaloneVdencModeEnable = a[14:15]
DecoderModeSelect = a[15:17]
DecoderShortFormatMode = a[17:18]
ExtendedStreamOutEnable = a[18:19]
Reserved51 = a[19:32]

print(StandardSelect);
print(CodecSelect);
print(StitchMode);
print(FrameStatisticsStreamoutEnable);
print(ScaledSurfaceEnable);
print(PreDeblockingOutputEnablePredeblockoutenable);
print(PostDeblockingOutputEnablePostdeblockoutenable);
print(StreamOutEnable);
print(PicErrorStatusReportEnable);
print(DeblockerStreamOutEnable);
print(VdencMode);
print(StandaloneVdencModeEnable);
print(DecoderModeSelect);
print(DecoderShortFormatMode);
print(ExtendedStreamOutEnable);
print(Reserved51);

print('done')