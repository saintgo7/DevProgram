// Game Framework

#include "Program096.h"

AProgram096::AProgram096()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram096::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Game Framework ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating game framework."));

    // Implement the program logic here...
}

void AProgram096::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
