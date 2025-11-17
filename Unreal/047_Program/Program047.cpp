// UMG

#include "Program047.h"

AProgram047::AProgram047()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram047::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== UMG ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating umg."));

    // Implement the program logic here...
}

void AProgram047::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
