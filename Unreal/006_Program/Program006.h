// Movement Component
// Program 006

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program006.generated.h"

UCLASS()
class AProgram006 : public AActor
{
    GENERATED_BODY()

public:
    AProgram006();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
