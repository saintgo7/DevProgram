// UMG
// Program 047

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program047.generated.h"

UCLASS()
class AProgram047 : public AActor
{
    GENERATED_BODY()

public:
    AProgram047();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
