// Sound Attenuation

#include "Program078.h"

AProgram078::AProgram078()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram078::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Sound Attenuation ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating sound attenuation."));

    // Implement the program logic here...
}

void AProgram078::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
