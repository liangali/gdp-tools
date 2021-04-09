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

a = BitArray('0x00020100')
StandardSelect = a[0:3]
CodecSelect = a[4:4]
StitchMode = a[5:5]
FrameStatisticsStreamoutEnable = a[6:6]
ScaledSurfaceEnable = a[7:7]
PreDeblockingOutputEnablePredeblockoutenable = a[8:8]
PostDeblockingOutputEnablePostdeblockoutenable = a[9:9]
StreamOutEnable = a[10:10]
PicErrorStatusReportEnable = a[11:11]
DeblockerStreamOutEnable = a[12:12]
VdencMode = a[13:13]
StandaloneVdencModeEnable = a[14:14]
DecoderModeSelect = a[15:16]
DecoderShortFormatMode = a[17:17]
ExtendedStreamOutEnable = a[18:18]
Reserved51 = a[19:31]

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