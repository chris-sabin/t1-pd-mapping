import itk
import numpy as np


def dicom_to_itk(dicom_folder, dimension=3, pixel_type=itk.F):
    '''
    Read a single dicom series as an itk image object. This function also
    returns the associated itk reader object, which is necessary for
    storing the dicom series' metadata.
    Default image type: 3 dimensional float.
    :param dicom_folder: path string
    :param dimension: int value
    :param pixel_type: itk c type
    :return itk_image: itk image object
    :return reader: itk image series reader object
    '''
    image_type = itk.Image[pixel_type, dimension]
    reader_type = itk.ImageSeriesReader[image_type]
    reader = reader_type.New()

    image_io_type = itk.GDCMImageIO
    dicom_io = image_io_type.New()
    dicom_io.LoadPrivateTagsOn()

    reader.SetImageIO(dicom_io)

    name_generator_type = itk.GDCMSeriesFileNames
    name_generator = name_generator_type.New()
    name_generator.SetUseSeriesDetails(True)
    name_generator.SetDirectory(dicom_folder)

    series_uid = name_generator.GetSeriesUIDs()
    if len(series_uid) > 1:
        raise Exception('Expected number of series in path directory is'
                        '1. The value was: {}'.format(len(series_uid)))
    filenames = name_generator.GetFileNames(series_uid[0])
    reader.SetFileNames(filenames)
    reader.MetaDataDictionaryArrayUpdateOn()
    reader.Update()
    itk_image = reader.GetOutput()
    return itk_image, reader