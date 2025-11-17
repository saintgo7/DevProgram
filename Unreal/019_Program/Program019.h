// UStaticMeshComponent
// Program 019

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program019.generated.h"

UCLASS()
class AProgram019 : public AActor
{
    GENERATED_BODY()

public:
    AProgram019();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
