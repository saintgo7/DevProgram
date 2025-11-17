// Input Mapping
// Program 009

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program009.generated.h"

UCLASS()
class AProgram009 : public AActor
{
    GENERATED_BODY()

public:
    AProgram009();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
