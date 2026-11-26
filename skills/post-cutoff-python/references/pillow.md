# pillow (pypi): changes after 2025-06-01

- Latest stable on the registry: **13.0.0** (2026-10-16). Built 2026-11-25.
- 7 stable releases after the cut-off: 11.3.0 (2025-07-01) to 13.0.0 (2026-10-16).
- New major versions since the cut-off: 12.0.0 (2025-10-15), 13.0.0 (2026-10-16).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 13.0.0 (2026-10-16) [source](https://github.com/python-pillow/Pillow/blob/main/docs/releasenotes/13.0.0.rst)
- Saving I mode images as PNG: In order to fit the 32 bits of I mode images into PNG, when PNG images can only contain at most 16 bits for a channel, Pillow has been clipping the values. […]
- Image.fromarray mode parameter: Using the `mode` parameter in `PIL.Image.fromarray()` was deprecated in Pillow 11.3.0. In Pillow 12.0.0, this was partially reverted, and now the only functionality removed is when the mode changes […]
- Image.Image.get_child_images(): `Image.Image.get_child_images()` has been moved to `ImageFile.ImageFile.get_child_images()`. The method uses an image's file pointer, and so child images could only be retrieved from an […]
- Image._show: `Image._show` has been removed. Use `PIL.ImageShow.show` instead.
- ImageCms.ImageCmsProfile.product_name and.product_info: `ImageCms.ImageCmsProfile.product_name` and the corresponding `.product_info` attributes have been removed. They were set to `None` since Pillow 2.3.0.
- ExifTags.IFD.Makernote: `ExifTags.IFD.Makernote` has been removed. Instead, use `ExifTags.IFD.MakerNote`.
- ImageColor.getcolor() with premultiplied alpha modes: When `mode` is `RGBa` or `La`, `PIL.ImageColor.getcolor` now returns color values premultiplied by the alpha channel, matching how pixels are stored in those modes. […]
- Duplicate TIFF tags: If a TIFF IFD contains the same tag more than once, the first value is now kept. Previously, the last value overwrote the earlier ones.
- Saving small ICO images: When saving an image smaller than 16x16 pixels as an ICO without a `sizes` argument, the image's own size is now used. […]
### 12.2.0 (2026-04-01) [source](https://github.com/python-pillow/Pillow/blob/main/docs/releasenotes/12.2.0.rst)
- Error when encoding an empty image: Attempting to encode an image with zero width or height would previously raise a `SystemError`. That has now been changed to a `ValueError`.
### 12.1.0 (2026-01-02) [source](https://github.com/python-pillow/Pillow/blob/main/docs/releasenotes/12.1.0.rst)
- ImageMorph build_default_lut(): To match the behaviour of `PIL.ImageMorph.LutBuilder.build_lut`, `PIL.ImageMorph.LutBuilder.build_default_lut()` now returns the new LUT.
### 12.0.0 (2025-10-15) [source](https://github.com/python-pillow/Pillow/blob/main/docs/releasenotes/12.0.0.rst)
- ImageFile.raise_oserror: `ImageFile.raise_oserror()` has been removed. The function was undocumented and was only useful for translating error codes returned by a codec's `decode()` method, which ImageFile already did […]
- IptcImageFile helper functions: The functions `IptcImageFile.dump` and `IptcImageFile.i`, and the constant `IptcImageFile.PAD` have been removed. […]
- ImageCms constants and versions() function: A number of constants and a function in `ImageCms` have been removed. This includes a table of flags based on LittleCMS version 1 which has been replaced with a new class […]
- ImageMath eval(): `ImageMath.eval()` has been removed. Use `PIL.ImageMath.lambda_eval` or `PIL.ImageMath.unsafe_eval` instead.
- BGR;15, BGR;16 and BGR;24: The experimental BGR;15, BGR;16 and BGR;24 modes have been removed.
- Non-image modes in ImageCms: The use in `ImageCms` of input modes and output modes that are not Pillow image modes has been removed. Defaulting to "L" or "1" if the mode cannot be mapped has also been removed.
- Support for LibTIFF earlier than 4: Support for LibTIFF earlier than version 4 has been removed. Upgrade to a newer version of LibTIFF instead.
- ImageDraw.getdraw hints parameter: The `hints` parameter in `PIL.ImageDraw.getdraw()` has been removed.
- FreeType 2.9.0: Support for FreeType 2.9.0 has been removed. FreeType 2.9.1 is the minimum version supported.
- Image.alpha_composite: LA images: `PIL.Image.alpha_composite` can now use LA images as well as RGBA.

## Removed or renamed
### 12.3.0 (2026-07-01) [source](https://github.com/python-pillow/Pillow/blob/main/docs/releasenotes/12.3.0.rst)
- Python 3.13 added an experimental free-threaded mode, and Pillow 11.0.0 added corresponding wheels. Now that Python 3.14 includes official support for it, Pillow has removed wheels for Python 3.13 free-threaded mode.

## Deprecated
### 13.0.0 (2026-10-16) [source](https://github.com/python-pillow/Pillow/blob/main/docs/releasenotes/13.0.0.rst)
- IM image format: The IM image format has been deprecated and removal is planned in Pillow 15.0.0 (2028-10-15). If you are using this format and would like to continue doing so, open an issue about what other software uses it.
- JpegImageFile.load_djpeg: `JpegImageFile.load_djpeg` has been deprecated, and will be removed in Pillow 14 (2027-10-15).
- ImageQt align8to32(): `ImageQt.align8to32()` has been deprecated. This was an undocumented helper function intended for internal use, so there is no replacement.
### 12.1.0 (2026-01-02) [source](https://github.com/python-pillow/Pillow/blob/main/docs/releasenotes/12.1.0.rst)
- Image getdata(): `PIL.Image.Image.getdata` has been deprecated. `PIL.Image.Image.get_flattened_data` can be used instead. This new method is identical, except that it returns a tuple of pixel values, instead of an internal Pillow […]
### 12.0.0 (2025-10-15) [source](https://github.com/python-pillow/Pillow/blob/main/docs/releasenotes/12.0.0.rst)
- Image._show: `Image._show` has been deprecated, and will be removed in Pillow 13 (2026-10-15). Use `PIL.ImageShow.show` instead.
- ImageCms.ImageCmsProfile.product_name and.product_info: `ImageCms.ImageCmsProfile.product_name` and the corresponding `.product_info` attributes have been deprecated, and will be removed in Pillow 13 (2026-10-15). […]
### 11.3.0 (2025-07-01) [source](https://github.com/python-pillow/Pillow/blob/main/docs/releasenotes/11.3.0.rst)
- Image.fromarray mode parameter: The `mode` parameter in `PIL.Image.fromarray()` has been deprecated. The mode can be automatically determined from the object's shape and type instead.
- Saving I mode images as PNG: In order to fit the 32 bits of I mode images into PNG, when PNG images can only contain at most 16 bits for a channel, Pillow has been clipping the values. […]

## Minimum versions and platform support
### 13.0.0 (2026-10-16) [source](https://github.com/python-pillow/Pillow/blob/main/docs/releasenotes/13.0.0.rst)
- Python 3.10: Pillow has dropped support for Python 3.10, which reached end-of-life in October 2026.
### 12.0.0 (2025-10-15) [source](https://github.com/python-pillow/Pillow/blob/main/docs/releasenotes/12.0.0.rst)
- Python 3.9: Pillow has dropped support for Python 3.9, which reached end-of-life in October 2025.

## Coverage
- Release notes read for 7 releases; 6 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 12.1.1.
- Sources: https://raw.githubusercontent.com/python-pillow/Pillow/main/docs/releasenotes/{version}.rst; registry (pypi) for dates.
