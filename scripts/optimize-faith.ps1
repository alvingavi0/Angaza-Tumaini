# Optimize images in filez/FAITH - create resized JPG and WebP variants
$sizes = @(1600,1200,800)
if (-not (Get-Command magick -ErrorAction SilentlyContinue)) {
    Write-Error "ImageMagick 'magick' not found on PATH. Install ImageMagick and re-run this script."
    exit 1
}
Get-ChildItem -Path .\filez\FAITH -Include *.jpg,*.jpeg -File | ForEach-Object {
    $name = $_.BaseName
    foreach ($w in $sizes) {
        $outJpg = "filez/FAITH/$name-$w.jpg"
        Write-Output "Creating $outJpg"
        magick $_.FullName -resize ${w}x -quality 82 $outJpg
        $outWebp = "filez/FAITH/$name-$w.webp"
        Write-Output "Creating $outWebp"
        magick $outJpg -quality 80 $outWebp
    }
}

Write-Output "FAITH image optimization complete."
