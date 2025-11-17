// Health Component

#include "Program042.h"

AProgram042::AProgram042()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram042::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Health Component ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating health component."));

    // Implement the program logic here...
}

void AProgram042::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
