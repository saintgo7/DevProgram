// Input Mapping

#include "Program009.h"

AProgram009::AProgram009()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram009::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Input Mapping ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating input mapping."));

    // Implement the program logic here...
}

void AProgram009::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
